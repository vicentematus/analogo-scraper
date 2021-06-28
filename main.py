from bs4 import BeautifulSoup


# se define el archivo, se define si se va a leer (r) o escribir (w)
with open('index.html', 'r') as html_file:
    content = html_file.read()
    # Se instancia BeautifulSoup primero se entrega el contenido, dsp el metodo de parser;
    soup = BeautifulSoup(content, 'lxml')

    # Busca todos los elementos y deja de buscar
    courses_html_tags = soup.find_all('h5')

    # buscamos el elemento, y podemos filtrar por algo en comun en especifico
    courses_cards = soup.find_all('div', class_='card')

    for course in courses_cards:
        course_name = course.h5.text
        # Guarda la informacion del precio del curso
        course_price = course.a.text.split()[-1]
        print(f'{course_name} cost {course_price}')
