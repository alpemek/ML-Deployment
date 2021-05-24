import torch
from PIL import Image
from torchvision.models.detection import retinanet_resnet50_fpn
from torchvision import transforms


DEVICE = torch.device("cuda")


COCO_INSTANCE_CATEGORY_NAMES = [
    '__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
    'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'N/A', 'stop sign',
    'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
    'elephant', 'bear', 'zebra', 'giraffe', 'N/A', 'backpack', 'umbrella', 'N/A', 'N/A',
    'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
    'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
    'bottle', 'N/A', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl',
    'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
    'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'N/A', 'dining table',
    'N/A', 'N/A', 'toilet', 'N/A', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
    'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'N/A', 'book',
    'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
]


class ObjectDetector():
    def __init__(self):

        self.image_transforms = transforms.Compose([
            transforms.ToTensor(),
            transforms.Resize(512),
        ])

        self.model = retinanet_resnet50_fpn(pretrained=True) #  pre-trained on COCO train2017
        self.model.eval()
        self.model.to(DEVICE)


    @torch.no_grad()
    def predict(self, input_image, score_threshold=0.5):
        input_image = input_image.convert('RGB')
        x = self.image_transforms(input_image)
        C, H, W = x.shape
        x = x.to(DEVICE)
        model_output = self.model(x[None])[0] # List[Dict[Tensor]] -> Dict[Tensor]

        result = []
        for label, box, score in  zip(model_output["labels"], model_output["boxes"], model_output["scores"]):
            if score.item() > score_threshold:
                result.append({
                    "label": COCO_INSTANCE_CATEGORY_NAMES[label.item()], 
                    "box": {k:round(v/scale, 2) for k, v, scale in zip(["x1", "y1", "x2", "y2"], box.tolist(), [W, H, W, H])} ,
                    "score": round(score.item(), 2)})

        return result


 
if __name__ == "__main__":
    det = ObjectDetector()
    image_path = "./example_image.png"
    im = Image.open(image_path) 
    output = det.predict(im)
    print(output)
    print(len(output))