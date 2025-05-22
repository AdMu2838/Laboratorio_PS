package ps.lab;

import java.util.Scanner;

public class Cajero {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        CajeroAutomatico cajero = new CajeroAutomatico(1000.0);

        int opcion;
        do {
            System.out.println("\n=== MENÚ CAJERO AUTOMÁTICO ===");
            System.out.println("1. Consultar Saldo");
            System.out.println("2. Depositar Dinero");
            System.out.println("3. Retirar Dinero");
            System.out.println("4. Salir");
            System.out.print("Seleccione una opción: ");

            while (!scanner.hasNextInt()) {
                System.out.println("Entrada inválida. Intente de nuevo:");
                scanner.next(); // descarta entrada inválida
            }
            opcion = scanner.nextInt();

            switch (opcion) {
                case 1:
                    System.out.printf("Saldo actual: S/.%.2f%n", cajero.consultarSaldo());
                    break;
                case 2:
                    System.out.print("Ingrese monto a depositar: ");
                    if (scanner.hasNextDouble()) {
                        double deposito = scanner.nextDouble();
                        try {
                            cajero.depositar(deposito);
                            System.out.println("Depósito realizado con éxito.");
                        } catch (IllegalArgumentException e) {
                            System.out.println("Error: " + e.getMessage());
                        }
                    } else {
                        System.out.println("Entrada inválida.");
                        scanner.next(); // descarta entrada inválida
                    }
                    break;
                case 3:
                    System.out.print("Ingrese monto a retirar: ");
                    if (scanner.hasNextDouble()) {
                        double retiro = scanner.nextDouble();
                        try {
                            cajero.retirar(retiro);
                            System.out.println("Retiro realizado con éxito.");
                        } catch (IllegalArgumentException e) {
                            System.out.println("Error: " + e.getMessage());
                        }
                    } else {
                        System.out.println("Entrada inválida.");
                        scanner.next(); // descarta entrada inválida
                    }
                    break;
                case 4:
                    System.out.println("Gracias por usar el cajero automático. ¡Hasta pronto!");
                    break;
                default:
                    System.out.println("Opción inválida. Intente nuevamente.");
            }

        } while (opcion != 4);

        scanner.close();
    }
}
