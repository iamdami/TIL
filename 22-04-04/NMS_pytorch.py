import torch

from IoU import intersection_over_union

def nms(bboxes, iou_threshold, threshold, box_format='corners'):

    # bboxes가 list인지 확인
    assert type(bboxes) == list

    # box 점수가 threshold보다 높은 것 선별
    # box shape는 [class, score, x1, y1, x2, y2]
    bboxes = [box for box in bboxes if box[1] > threshold]
    # 점수 오름차순 정렬
    bboxes = sorted(bboxes, key=lambda x: x[1], reverse=True)
    bboxes_after_nmn = []

    # bboxes 모두 제거될 때 까지 반복
    while bboxes:
        # 0번째 index 가장 높은 점수 갖고있는 box 선택 후 bboxes에서 제거
        chosen_box = bboxes.pop(0)

        # box가 선택된 box와의 iou가 임계치보다 낮거나
        # class가 다르면 bboxes에 남기고 그 외는 제거
        bboxes = [box for box in bboxes if box[0] != chosen_box[0] \
               or intersection_over_union(torch.tensor(chosen_box[2:]),
                                          torch.tensor(box[2:]),
                                          box_format=box_format)
                    < iou_threshold]

        # 선택된 박스 추가
        bboxes_after_nmn.append(chosen_box)

    return bboxes_after_nmn
