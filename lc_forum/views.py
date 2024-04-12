from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from machina.apps.forum.models import Forum
from machina.apps.forum_conversation.models import Topic, Post
from .serializers import ForumSerializer, TopicSerializer, PostSerializer, AttachmentSerializer
from .models import ForumAccess
from machina.apps.forum_conversation.forum_attachments.models import Attachment

class ForumViewSet(viewsets.ModelViewSet):
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Forum.objects.all()
        else:
            accessible_forums = ForumAccess.objects.filter(
                user=self.request.user, can_access=True
            ).values_list('forum_id', flat=True)
            return Forum.objects.filter(id__in=accessible_forums)
        

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        accessible_forums = ForumAccess.objects.filter(
            user=self.request.user, can_access=True
        ).values_list('forum_id', flat=True)
        return Topic.objects.filter(forum_id__in=accessible_forums)

    def perform_create(self, serializer):
        print("Received data:", self.request.data)
        print("Creating topic with data:", serializer.validated_data)
        if not Forum.objects.filter(pk=1).exists():
            print("No forum with ID 1 found.")

        serializer.save(poster=self.request.user)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        accessible_Topics = Topic.objects.filter(
            forum_id__in=ForumAccess.objects.filter(
                user=self.request.user, can_access=True
            ).values_list('forum_id', flat=True)
        ).values_list('id', flat=True)
        return Post.objects.filter(Topic_id__in=accessible_Topics)
    
    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)

class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Attachment.objects.all()
        user_posts = Post.objects.filter(poster=self.request.user).values_list('id', flat=True)
        return Attachment.objects.filter(post_id__in=user_posts)

    def perform_create(self, serializer):
        serializer.save()
