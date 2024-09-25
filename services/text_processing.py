import easyocr
import os

os.makedirs('/app/.EasyOCR', exist_ok=True)
os.environ['EASYOCR_CACHE_DIR'] = '/app/.EasyOCR'
text_reader = easyocr.Reader(['en'], model_storage_directory=os.environ['EASYOCR_CACHE_DIR'])

def adjust_image_to_get_text(image,x,y,w,h,y_th):
    new_im = image[y:y+h+y_th,x-5:x+w]
    result = text_reader.readtext(new_im)
    if len(result) > 1:
        return adjust_image_to_get_text(image,x,y,w,h,y_th-5)
    return result


def get_texts(img,contours):
    products = []
    product = {}
    for i, v in enumerate(contours):
        _,(x,y,w,h) = v
        result = adjust_image_to_get_text(img,x,y,w,h,5)
        if result:
            if i % 2 != 0:
                product['cost'] = ''.join(result[0][1].split())
                products.append(product)
                product = {}
            else:
                product['name'] =  ' '.join(result[0][1].split())
    return products
        
