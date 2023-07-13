import boto3
from botocore.exceptions import NoCredentialsError

def download_file_from_s3(bucket_name, remote_filename, local_filename):
    try:
        s3 = boto3.client('s3')
        s3.download_file(bucket_name, remote_filename, local_filename)
        print(f"Файл {remote_filename} успешно загружен в {local_filename}")
    except NoCredentialsError:
        print("Не удалось найти учетные данные AWS.")

def generate_photo_album(album_name, photo_urls):
    html_content = f"<h1>{album_name}</h1>\n"
    for url in photo_urls:
        html_content += f"<img src='{url}' alt='Фотоальбом'>\n"
    with open("photo_album.html", "w") as file:
        file.write(html_content)
    print("HTML-страница с фотоальбомом успешно сгенерирована.")

def main():
    # Настройки AWS
    aws_access_key_id = 'ВАШ_ACCESS_KEY_ID'
    aws_secret_access_key = 'ВАШ_SECRET_ACCESS_KEY'
    bucket_name = 'ИМЯ_BUCKET'
    album_name = 'Название фотоальбома'

    # Список фотографий в Yandex Object Storage
    photo_filenames = ['photo1.jpg', 'photo2.jpg', 'photo3.jpg']

    # Загрузка файлов из Yandex Object Storage
    for filename in photo_filenames:
        remote_filename = f'{album_name}/{filename}'  # Путь к файлу в облаке
        local_filename = f'downloaded_photos/{filename}'  # Путь для сохранения файла локально
        download_file_from_s3(bucket_name, remote_filename, local_filename)

    # Генерация HTML-страницы с фотоальбомом
    photo_urls = [f'downloaded_photos/{filename}' for filename in photo_filenames]
    generate_photo_album(album_name, photo_urls)

if __name__ == '__main__':
    main()