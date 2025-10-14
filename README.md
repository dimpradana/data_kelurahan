* Modul 5: Konsep Fundamental API & Dunia JSON

*   **Arsitektur:** Pindah dari Monolitik ke Decoupled (API Backend + Frontend Terpisah).
*   **API:** Perantara komunikasi antar aplikasi (Analogi: Pelayan Restoran).
*   **REST:** Gaya arsitektur API (berbasis resource, pakai HTTP verbs: GET, POST, PUT, DELETE, stateless).
*   **JSON:** Format data ringan untuk pertukaran (mirip dictionary/list Python).
*   **Praktik:** Menggunakan Postman untuk berinteraksi dengan API publik (`reqres.in`).
    *   GET /api/users -> List users (Status 200 OK)
    *   GET /api/users/2 -> Detail user (Status 200 OK)
    *   POST /api/users -> Create user (Status 201 Created)
    *   GET /api/users/99 -> Not Found (Status 404 Not Found)