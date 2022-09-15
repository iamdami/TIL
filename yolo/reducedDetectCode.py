import torch
from models.common import DetectMultiBackend
from utils.general import (check_img_size, non_max_suppression, scale_coords)
from utils.dataloaders import LoadImages


def main():
    weights = "fallDown.pt"
    source = "asd.jpg"
    data = "fallDown.yaml"

    model = DetectMultiBackend(weights, device = torch.device("cuda:0"))
    stride, names, pt = model.stride, model.names, model.pt
    imgsz = check_img_size((640, 640), s = stride)
    
    dataset = LoadImages(source, img_size = imgsz, stride = stride, auto = pt)
    
    pointList = list()

    for path, im, im0s in dataset:
        im = torch.from_numpy(im).to(torch.device("cuda:0"))
        im = im/half() if model.fp16 else im.float()
        im /= 255
        if len(im.shape) == 3:
            im = im[None]
        
        pred = model(im, augment = False, visualize = False)
        pred = non_max_suppression(pred, 0.25, 0.45, None, False, max_det = 1000)

        for i, det in enumerate(pred):
            p, im0, frame = path, im0s.copy(), getattr(dataset, "frame", 0)

            if len(det):
                det[:, :4] = scale_coords(im.shape[2:], det[:, :4], im0.shape).round()

                for c in det[:, -1].unique():
                    pointList.append(names[int(c)])
                
                for *xyxy, conf, cls in reversed(det):
                    xyxy = list(map(int, xyxy))
                    print(xyxy)
                pass

    return pointList
    
main()
