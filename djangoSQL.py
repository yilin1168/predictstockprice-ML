from django.db.models import Case, When, Sum, Value, F, FloatField
from .models import Transaction

# 对Transaction模型进行聚合计算
result = Transaction.objects.annotate(
    total=Sum(
        Case(
            When(amount_a__isnull=False, then=F('amount_a')),
            When(amount_b__isnull=False, then=F('amount_b')),
            default=Value(0),  # 如果两列都是空的，则默认值为0
            output_field=FloatField()  # 确保输出类型与你的字段类型匹配
        )
    )
)

print(result.aggregate(sum_total=Sum('total'))['sum_total'])
