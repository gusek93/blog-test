from django.db.models import Q
from .serializers import PostSerializer
from .models import Post
from users.models import User
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_queryset(self):
        search_keyword = self.request.GET.get('keyword', '')
        search_list = self.queryset

        if search_keyword:
            if len(search_keyword) > 1:
                search_notice_list = search_list.filter(
                    Q (title__icontains=search_keyword) |
                    Q (body__icontains=search_keyword)
                )
                return search_notice_list
            else:
                print(self.request, '검색어는 2글자 이상 입력해주세요')

        return search_list

    def get_object(self, pk=None):
        try:
            return self.queryset.get(pk=pk)
        except Post.DoesNotExist:
            raise NotFound('Not Found')


    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={'user':request.user}
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def list(self, request, *args, **kwargs):
        page = self.paginate_queryset(self.get_queryset())
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)


    def retrieve(self, request, pk=None, *args, **kwargs):
        post = self.get_object(pk)
        serializer = self.serializer_class(post)
        return Response(serializer.data)


    def update(self, request, pk=None, *args, **kwargs):
        post = self.get_object(pk)
        serializer = self.serializer_class(
            post,
            data=request.data,
            context={'uset': request.user},
            partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


    def destroy(self, request, pk=None, *args, **kwargs):
        user = self.get_object(pk)
        user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)