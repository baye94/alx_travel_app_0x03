## 💳 Chapa Payment Integration

- Initiate Payment: `POST /api/initiate-payment/`
- Verify Payment: `GET /api/verify-payment/?tx_ref=...`

### Environment Variables
- `CHAPA_SECRET_KEY` – Your Chapa API secret key

### Payment Statuses
- `Pending`: Payment initialized
- `Completed`: Payment successful
- `Failed`: Payment unsuccessful
