from rest_framework import serializers
from machina.apps.forum.models import Forum
from machina.apps.forum_conversation.models import Topic
from machina.apps.forum_conversation.models import Post
from machina.apps.forum_conversation.forum_attachments.models import Attachment

class ForumSerializer(serializers.ModelSerializer):
    parent = serializers.SlugRelatedField(slug_field='name', read_only=True)
    last_post = serializers.SlugRelatedField(slug_field='subject', read_only=True)

    class Meta:
        model = Forum
        fields = [
            'id', 'name', 'slug', 'description', 'image', 'link', 'link_redirects',
            'type', 'direct_posts_count', 'direct_topics_count', 'link_redirects_count',
            'last_post', 'last_post_on', 'display_sub_forum_list', 'parent'
        ]
        read_only_fields = ['direct_posts_count', 'direct_topics_count', 'link_redirects_count', 'last_post_on']

class TopicSerializer(serializers.ModelSerializer):
    poster = serializers.SlugRelatedField(slug_field='username', read_only=True)
    forum = serializers.SlugRelatedField(slug_field='name', read_only=True)
    first_post_subject = serializers.ReadOnlyField(source='first_post.subject')
    last_post_subject = serializers.ReadOnlyField(source='last_post.subject')

    class Meta:
        model = Topic
        fields = [
            'id', 'forum', 'poster', 'subject', 'slug', 'type', 'status', 'approved',
            'posts_count', 'views_count', 'last_post_on', 'first_post_subject', 
            'last_post_subject', 'created', 'updated'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request', None)
        if request and request.method in ['GET']:
            self.fields['forum'] = serializers.SlugRelatedField(slug_field='name', read_only=True)
        else:
            self.fields['forum'] = serializers.PrimaryKeyRelatedField(queryset=Forum.objects.all())

class PostSerializer(serializers.ModelSerializer):
    poster = serializers.SlugRelatedField(slug_field='username', read_only=True)
    topic_subject = serializers.ReadOnlyField(source='topic.subject')

    class Meta:
        model = Post
        fields = [
            'id', 'topic', 'topic_subject', 'poster', 'subject', 'content', 'approved',
            'enable_signature', 'update_reason', 'updated_by', 'updates_count', 'created'
        ]

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ['id', 'post', 'file', 'comment']

    def create(self, validated_data):
        return Attachment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.comment = validated_data.get('comment', instance.comment)
        instance.file = validated_data.get('file', instance.file)
        instance.save()
        return instance