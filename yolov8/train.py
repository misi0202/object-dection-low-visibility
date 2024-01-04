from ultralytics import YOLO

# 训练模型
if __name__=="__main__":
    # 加载模型
    model = YOLO('yolov8n.yaml')  # 从YAML构建新模型
    model = YOLO('yolov8n.pt')    # 加载预训练模型（推荐用于训练）
    model = YOLO('yolov8n.yaml').load('yolov8n.pt')  # 从YAML构建并转移权重
    results = model.train(data='D:\python_code\od\yolov8\Exdark.yaml', epochs=10, imgsz=640)