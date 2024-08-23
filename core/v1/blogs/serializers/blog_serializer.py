from rest_framework import serializers

from ..models import Blog


class BlogCreateRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ["title", "content", "main_image"]
        extra_kwargs = {"title": {"required": True}, "content": {"required": True}}

    def create(self, validated_data):
        blog = Blog.objects.create(**validated_data)
        return blog


class BlogUpdateRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ["title", "content", "main_image"]

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        if "main_image" in validated_data:
            instance.main_image = validated_data["main_image"]
        instance.save()
        return instance


class BlogResponseSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Blog
        fields = [
            "id",
            "title",
            "content",
            "slug",
            "created_at",
            "updated_at",
            "main_image",
            "author",
        ]
