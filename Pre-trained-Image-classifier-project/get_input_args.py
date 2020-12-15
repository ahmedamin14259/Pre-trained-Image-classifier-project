import argparse

def get_input_args():
    
    parser = argparse.ArgumentParser()

    parser.add_argument('--dir', type=str, default='pet_images/', help='Path to the folder of pet images')
    parser.add_argument('--arch', type=str, default='vgg', help='Choose CNN model for classification')
    parser.add_argument('--dogfile', type=str, default='dognames.txt', help='File that contains alll lanbels associated to dogs')

    return parser.parse_args()
