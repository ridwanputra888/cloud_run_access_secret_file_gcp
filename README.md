# Cloud Run Secret Test

Proyek ini mendemonstrasikan cara menggunakan **Google Cloud Secret Manager** untuk menyimpan file rahasia dan mengaksesnya dari **Cloud Run**.

---

## 🚀 Jalankan secara lokal

Build dan jalankan container dengan mounting file `my-secret.json`:

```bash
docker run -it --rm \
  -p 9090:8080 \
  -v $(pwd)/my-secret.json:/secrets/my-secret.json \
  cloudrun-secret-test
```

Lalu buka di browser:

- [http://127.0.0.1:9090/](http://127.0.0.1:9090/) → **Cloud Run Secret Test: service is running!**
- [http://127.0.0.1:9090/check-secret](http://127.0.0.1:9090/check-secret) → ✅ Secret file is accessible!  
  Output contoh:
  ```json
  {"test_key": "hello_from_local"}
  ```

---

## 📦 Build dan Push ke Artifact Registry

Gunakan perintah berikut untuk build dan push image ke **Artifact Registry**:

```bash
gcloud builds submit \
  -t {{region}}.pkg.dev/{{project_id}}/test-secret/cloudrun-secret-test .
```

---

## 🔑 Buat Secret di Secret Manager

1. Buka [Secret Manager Console](https://console.cloud.google.com/security/secret-manager).
2. Klik **Create Secret**.
3. Isi **name**.
4. Upload file `my-secret.json` melalui **Browse**.
5. Klik **Create Secret**.

---

## ☁️ Deploy ke Cloud Run

Deploy service ke **Cloud Run** dengan menghubungkan secret:

```bash
gcloud run deploy cloudrun-secret-test \
  --image {{region}}-docker.pkg.dev/{{project_id}}/test-secret/cloudrun-secret-test \
  --region us-central1 \
  --allow-unauthenticated \
  --set-secrets /secrets/my-secret.json=my_secret_file:latest
  --set-env-vars SECRET_PATH=/secrets/my-secret.json
```

---

## ✅ Verifikasi

Setelah deploy selesai, buka URL Cloud Run-mu:

- `/` → menampilkan pesan: **service is running!**
- `/check-secret` → menampilkan isi awal file secret dari Secret Manager.
