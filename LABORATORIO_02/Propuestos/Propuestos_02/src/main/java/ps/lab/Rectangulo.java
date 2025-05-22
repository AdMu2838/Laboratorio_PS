package ps.lab;

public class Rectangulo {
    public static double calcularArea(double ancho, double alto) {
        if (ancho < 0 || alto < 0) {
            throw new IllegalArgumentException("Las dimensiones deben ser no negativas");
        }
        return ancho * alto;
    }
}
