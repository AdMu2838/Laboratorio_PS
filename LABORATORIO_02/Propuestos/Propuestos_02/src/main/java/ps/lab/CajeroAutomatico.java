package ps.lab;
public class CajeroAutomatico {
    private double saldo;

    public CajeroAutomatico(double saldoInicial) {
        if (saldoInicial < 0) {
            throw new IllegalArgumentException("El saldo inicial no puede ser negativo.");
        }
        this.saldo = saldoInicial;
    }

    public double consultarSaldo() {
        return saldo;
    }

    public void depositar(double cantidad) {
        if (cantidad <= 0) {
            throw new IllegalArgumentException("El depósito debe ser mayor a cero.");
        }
        saldo += cantidad;
    }

    public void retirar(double cantidad) {
        if (cantidad <= 0) {
            throw new IllegalArgumentException("El retiro debe ser mayor a cero.");
        }
        if (cantidad > saldo) {
            throw new IllegalArgumentException("Fondos insuficientes.");
        }
        saldo -= cantidad;
    }
}

