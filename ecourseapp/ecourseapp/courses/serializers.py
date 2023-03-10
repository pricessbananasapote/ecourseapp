from rest_framework import serializers

from .models import Category, Course, Lesson, Tag


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class CourseSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(source='image')

    def get_image(self, course):  # link dẫn zô image#
        if course.image:
            request = self.context.get('request')
            return request.build_absolute_uri('/static/%s' % course.image.name) if request else ''

    class Meta:
        model = Course
        fields = ['id', 'subject', 'description', 'image', 'created_date', 'category_id']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class LessonSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(source='image')

    def get_image(self, lesson):  # link dẫn zô image#
        if lesson.image:
            request = self.context.get('request')
            return request.build_absolute_uri('/static/%s' % lesson.image.name) if request else ''

    class Meta:
        model = Lesson
        fields = ['id', 'subject', 'created_date', 'updated_date', 'image']


class LessonDetailsSerializer(LessonSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = LessonSerializer.Meta.model
        fields = LessonSerializer.Meta.fields + ['content', 'tags']
