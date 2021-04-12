from PIL import Image, ImageDraw
import numpy as np
import time

#batch_data['rgb']

#S_numpy.shape[1]

def draw(type_feature, rgb, switches_2d_argsort, shape_1):

    print("Drawing")
    hor = switches_2d_argsort % shape_1
    ver = np.floor(switches_2d_argsort // shape_1)
    # print(ver[:10], hor[:10])
    # print("and")
    # print(ver[-10:], hor[-10:])

    ma = rgb.detach().cpu().numpy().squeeze()
    ma = np.transpose(ma, axes=[1, 2, 0])
    # ma = np.uint8(ma)
    # ma2 = Image.fromarray(ma)
    ma2 = Image.fromarray(np.uint8(ma)).convert('RGB')
    # create rectangle image
    img1 = ImageDraw.Draw(ma2)

    if type_feature == "sq":
        size = 40

        for ii in range(len(switches_2d_argsort)):
            s_hor = hor[ii]#.detach().cpu().numpy()
            s_ver = ver[ii]#.detach().cpu().numpy()
            # print("Top square switches: ")
            # print(s_ver, s_hor)
            shape = [(s_hor * size, s_ver * size), ((s_hor + 1) * size, (s_ver + 1) * size)]
            # print("shape: ", shape)

            img1.rectangle(shape, outline="red")

        tim = time.time()
        lala = ma2.save(f"switches_photos/squares/squares_{tim}.jpg")
        print("saving")
    elif type_feature == "lines":
        print_square_num = 20
        r = 1
        parameter_mask = np.load("../kitti_pixels_to_lines.npy", allow_pickle=True)

        # for m in range(10,50):
        #     im = Image.fromarray(parameter_mask[m]*155)
        #     im = im.convert('1')  # convert image to black and white
        #     im.save(f"switches_photos/lala_{m}.jpg")

        for ii in range(print_square_num):
            points = parameter_mask[ii]
            y = np.where(points == 1)[0]
            x = np.where(points == 1)[1]

            for p in range(len(x)):
                img1.ellipse((x[p] - r, y[p] - r, x[p] + r, y[p] + r), fill=(255, 0, 0, 0))

        lala = ma2.save(f"switches_photos/lines/lines_{tim}.jpg")
        print("saving")