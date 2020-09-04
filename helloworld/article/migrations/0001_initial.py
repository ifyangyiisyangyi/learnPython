# Generated by Django 3.0.6 on 2020-09-04 15:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='About 内容')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'About',
            },
        ),
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(help_text='编号决定图片播放的顺序，图片不要多于5张', verbose_name='编号')),
                ('title', models.CharField(blank=True, help_text='标题可以为空', max_length=20, null=True, verbose_name='标题')),
                ('content', models.CharField(max_length=80, verbose_name='描述')),
                ('img_url', models.CharField(max_length=200, verbose_name='图片地址')),
                ('url', models.CharField(default='#', help_text='图片跳转的超链接，默认#表示不跳转', max_length=200, verbose_name='跳转链接')),
            ],
            options={
                'verbose_name': '图片轮播',
                'verbose_name_plural': '图片轮播',
                'ordering': ['number', '-id'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='文章分类')),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(max_length=240, verbose_name='描述')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='FriendLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='网站名称')),
                ('description', models.CharField(blank=True, max_length=100, verbose_name='网站描述')),
                ('link', models.URLField(help_text='请填写http或https开头的完整形式地址', verbose_name='友链地址')),
                ('logo', models.URLField(blank=True, help_text='请填写http或https开头的完整形式地址', verbose_name='网站LOGO')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否有效')),
                ('is_show', models.BooleanField(default=False, verbose_name='是否首页展示')),
            ],
            options={
                'verbose_name': '友情链接',
                'verbose_name_plural': '友情链接',
                'ordering': ['create_date'],
            },
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='文章关键词')),
            ],
            options={
                'verbose_name': '关键词',
                'verbose_name_plural': '关键词',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Silian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('badurl', models.CharField(help_text='注意：地址是以http开头的完整链接格式', max_length=200, verbose_name='死链地址')),
                ('remark', models.CharField(blank=True, max_length=50, null=True, verbose_name='死链说明')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='提交日期')),
            ],
            options={
                'verbose_name': '死链',
                'verbose_name_plural': '死链',
                'ordering': ['-add_date'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='文章标签')),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(max_length=240, verbose_name='描述')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('side', models.CharField(choices=[('L', '左边'), ('R', '右边')], default='L', max_length=1, verbose_name='位置')),
                ('star_num', models.IntegerField(choices=[(1, '1颗星'), (2, '2颗星'), (3, '3颗星'), (4, '4颗星'), (5, '5颗星')], default=3, verbose_name='星星个数')),
                ('icon', models.CharField(default='fa fa-pencil', max_length=50, verbose_name='图标')),
                ('icon_color', models.CharField(choices=[('primary', '基本-蓝色'), ('success', '成功-绿色'), ('info', '信息-天蓝色'), ('warning', '警告-橙色'), ('danger', '危险-红色')], default='info', max_length=20, verbose_name='图标颜色')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('update_date', models.DateTimeField(verbose_name='更新时间')),
                ('content', models.TextField(verbose_name='主要内容')),
            ],
            options={
                'verbose_name': '时间线',
                'verbose_name_plural': '时间线',
                'ordering': ['update_date'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='文章标题')),
                ('summary', models.TextField(default='文章摘要等同于网页description内容，请务必填写...', max_length=230, verbose_name='文章摘要')),
                ('body', models.TextField(verbose_name='文章内容')),
                ('img_link', models.CharField(default='/static/blog/img/summary.png', max_length=255, verbose_name='图片地址')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('views', models.IntegerField(default=0, verbose_name='阅览量')),
                ('slug', models.SlugField(unique=True)),
                ('is_top', models.BooleanField(default=False, verbose_name='置顶')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='article.Category', verbose_name='文章分类')),
                ('keywords', models.ManyToManyField(help_text='文章关键词，用来作为SEO中keywords，最好使用长尾词，3-4个足够', to='article.Keyword', verbose_name='文章关键词')),
                ('tags', models.ManyToManyField(to='article.Tag', verbose_name='标签')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'ordering': ['-create_date'],
            },
        ),
    ]
