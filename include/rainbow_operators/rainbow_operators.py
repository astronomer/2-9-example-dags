# import the operator to inherit from
from airflow.models.baseoperator import BaseOperator

class ExtractFromObjectStorageOperator(BaseOperator):
    ui_color = "#e39f9f"

    def __init__(self, my_param, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def execute(self, context):
        return "hi :)"


class TransformOperator(BaseOperator):
    ui_color = "#ffc175"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def execute(self, context):
        return "hi :)"
    

class LoadtoDWHOperator(BaseOperator):
    ui_color = "#fff9ad"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def execute(self, context):
        return "hi :)"
    

class LoadAPItoDWHOperator(BaseOperator):
    ui_color = "#a8f0bd"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def execute(self, context):
        return "hi :)"
    
class TransformReportOperator(BaseOperator):
    ui_color = "#96a7d6"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def execute(self, context):
        return "hi :)"
    

class PublishReportOperator(BaseOperator):
    ui_color = "#bd97c4"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def execute(self, context):
        return "hi :)"
    
# 
    

class SpinUpGPUOperator(BaseOperator):
    ui_color = "#bfedff"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def execute(self, context):
        return "hi :)"
    

class TrainProprietaryLLMOperator(BaseOperator):
    ui_color = "#f7c3ce"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def execute(self, context):
        return "hi :)"
    

class TearDownGPUOperator(BaseOperator):
    ui_color = "#FFFFFF"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def execute(self, context):
        return "hi :)"