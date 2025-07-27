def load_image(image_path):
    import cv2
    image = cv2.imread(image_path)
    return image

def save_output(output_path, data):
    with open(output_path, 'w') as file:
        file.write(data)