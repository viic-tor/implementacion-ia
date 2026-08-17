import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10, // Simula 10 usuarios al mismo tiempo
  duration: '30s', // La prueba durara 30 segundos
};

export default function () {
  const url = 'http://host.docker.internal:8000/clasificar';
  const payload = JSON.stringify({
    texto: 'implementa nueva funcion de pagos',
    motor: 'eco'
  });

  const params = {
    headers: {
      'Content-Type': 'application/json',
    },
  };

  const res = http.post(url, payload, params);
  check(res, {
    'estado es 200': (r) => r.status === 200,
  });
  sleep(1);
}
