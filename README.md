# Netflix Clone with Django

Bu proje, Django, Python, HTML, CSS, JavaScript ve Bootstrap 5 kullanılarak geliştirilmiş bir Netflix klonudur.

## Projeyi Çalıştırma

1. Proje klasörünü klonlayın:

    ```bash
    git clone https://github.com/kullaniciadi/netflix-clone.git
    ```

2. Proje dizinine gidin:

    ```bash
    cd netflix-clone
    ```

3. Virtual environment'ı oluşturun:

    ```bash
    python -m venv venv
    ```

4. Virtual environment'ı etkinleştirin:

    - Windows:

        ```bash
        venv\Scripts\activate
        ```

    - Linux/Mac:

        ```bash
        source venv/bin/activate
        ```

5. Gerekli bağımlılıkları yükleyin:

    ```bash
    pip install -r requirements.txt
    ```

6. Veritabanını oluşturun ve migrasyonları uygulayın:

    ```bash
    python manage.py migrate
    ```

7. Django projesini başlatın:

    ```bash
    python manage.py runserver
    ```

8. Tarayıcınızda [http://localhost:8000](http://localhost:8000) adresine gidin.

## Azure'a Dağıtma

Projeyi Azure'a dağıtmak için şu adımları takip edebilirsiniz:

1. [Azure Portal](https://portal.azure.com/) üzerinden yeni bir Web App oluşturun.

2. Deployment Center bölümünde GitHub'u seçin ve GitHub hesabınızı bağlayın.

3. Projenizi seçin ve otomatik dağıtım için yapılandırma yapın.

4. Azure, projenizi otomatik olarak dağıtacaktır.

## Whitenoise Eklemek ve Static Dosyaları Toplamak

1. `whitenoise`'ı yükleyin:

    ```bash
    pip install whitenoise
    ```

2. `settings.py` dosyasına şu satırı ekleyin:

    ```python
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    ```

3. `requirements.txt` dosyasını oluşturun:

    ```bash
    pip freeze > requirements.txt
    ```

4. Static dosyaları toplayın:

    ```bash
    python manage.py collectstatic
    ```

5. Azure'da bu değişiklikleri uygulayın ve tekrar dağıtım yapın.

Bu adımlar genel bir rehber niteliğindedir ve projenizin özel ihtiyaçlarına göre uyarlamalar yapmanız gerekebilir. Ayrıca, Azure üzerindeki özel konfigürasyonlarınızı belirtmek için Azure portalındaki belgeleri kontrol etmeniz önemlidir.

Proje hakkında geri bildirimleriniz veya katkılarınız varsa lütfen iletişime geçmekten çekinmeyin. İyi kodlamalar!

