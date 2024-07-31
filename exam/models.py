from django.db import models

# Create your models here.

class Topic(models.Model):
    # 主题ID，自增主键
    T_id = models.AutoField(primary_key=True)
    # 主题名，字符串类型，最大长度100
    T_name = models.CharField(max_length=100)
    # 主题下题目数量，整数类型
    T_count = models.IntegerField(default=0)

    def __str__(self):
        return self.T_name

class Question(models.Model):
    # 题目编号，自增主键
    Q_id = models.AutoField(primary_key=True)
    # 上传时间，创建时自动设置
    Q_add_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    # 修改时间，每次保存模型时自动更新
    Q_edit_time = models.DateTimeField(auto_now=True, auto_now_add=False)
    # 题目类型，使用choices选项来定义
    Q_TYPE_CHOICES = (
        ('A', '单选题'),
        ('B', '多选题'),
        ('C', '判断题'),
        ('D', '填空题'),
        ('E', '计算题'),
        ('F', '问答题'),
    )
    Q_type = models.CharField(
        max_length=1,
        choices=Q_TYPE_CHOICES
    )
    # 题面，字符串类型，最大长度500
    Q_content = models.CharField(max_length=500)
    # 选项数量，整数类型
    Q_choice_num = models.IntegerField()
    # 选项A，字符串类型，最大长度500
    Q_choice_A = models.CharField(max_length=500)
    # 选项B，字符串类型，最大长度500
    Q_choice_B = models.CharField(max_length=500)
    # 选项C，字符串类型，最大长度500
    Q_choice_C = models.CharField(max_length=500)
    # 选项D，字符串类型，最大长度500
    Q_choice_D = models.CharField(max_length=500)
    # 答案，字符串类型，最大长度5000
    Q_answer = models.CharField(max_length=5000)
    # 题目来源，字符串类型，最大长度500
    Q_source = models.CharField(max_length=500)
    # 对应Topic表中的T_id，字符串类型，最大长度10
    T_id = models.CharField(max_length=10)

    def __str__(self):
        return self.Q_content