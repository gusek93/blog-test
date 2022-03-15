from rest_framework import serializers
from .models import Post
from users.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


    def create(self, validate_data):
        user = self.context.pop('user')

        return Post.objects.create(
            user=user,
            **validate_data,
        )

    def update(self, instance, validate_data):
        user = self.context.get('user')

        for(key, value) in validate_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance

