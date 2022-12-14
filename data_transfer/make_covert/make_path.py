import os


def get_args():
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--images', help="images path",
                        type=str, default='E:/yolor-main/yolor-main/bdd100k/train/images')
    parser.add_argument('-t', '--type', help="type of dataset",
                        choices=['train', 'val'], default='train')

    return parser.parse_args()


def getFileList(dir, extract):
    fileList = []
    filenames = os.listdir(dir)
    for filename in filenames:
        ext = os.path.splitext(filename)[-1]
        if ext == extract:
            fileList.append(filename)
    return fileList


if __name__ == '__main__':
    args = get_args()

    if args.type == 'train':
        imageRootPath = os.path.join(args.images, 'train')
    else:
        imageRootPath = os.path.join(args.images, 'val')

    imageName = getFileList(imageRootPath, '.jpg')
    labelName = getFileList(imageRootPath, '.txt')

    labelName = [label.replace(".txt", ".jpg") for label in labelName]
    lackImages = set(imageName) - set(labelName)

    for file in lackImages:
        os.remove(os.path.join(imageRootPath,file))
        #print(os.path.join(imageRootPath,file))