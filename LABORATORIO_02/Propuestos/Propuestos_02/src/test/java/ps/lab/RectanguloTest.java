package ps.lab;


import org.junit.Test;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.*;

public class RectanguloTest {

    // Casos normales
    @Test public void area_5x10() {
        assertThat(Rectangulo.calcularArea(5, 10), is(50.0));
    }
    @Test public void area_2x3() {
        assertThat(Rectangulo.calcularArea(2, 3), is(6.0));
    }
    @Test public void area_decimal() {
        assertThat(Rectangulo.calcularArea(2.5, 4), is(10.0));
    }
    @Test public void area_decimalAmbos() {
        assertThat(Rectangulo.calcularArea(2.5, 1.2), closeTo(3.0, 0.0001));
    }

    // Casos con cero
    @Test public void area_anchoCero() {
        assertThat(Rectangulo.calcularArea(0, 5), is(0.0));
    }
    @Test public void area_altoCero() {
        assertThat(Rectangulo.calcularArea(5, 0), is(0.0));
    }
    @Test public void area_ambosCero() {
        assertThat(Rectangulo.calcularArea(0, 0), is(0.0));
    }

    // Casos negativos (excepciones esperadas)
    @Test(expected = IllegalArgumentException.class)
    public void area_anchoNegativo() { Rectangulo.calcularArea(-1, 5); }

    @Test(expected = IllegalArgumentException.class)
    public void area_altoNegativo() { Rectangulo.calcularArea(5, -1); }

    @Test(expected = IllegalArgumentException.class)
    public void area_ambosNegativos() { Rectangulo.calcularArea(-5, -5); }

    // Casos límite y precisión
    @Test public void area_valoresPequeños() {
        assertThat(Rectangulo.calcularArea(0.0001, 0.0001), closeTo(0.00000001, 0.00000001));
    }

    @Test public void area_valoresGrandes() {
        assertThat(Rectangulo.calcularArea(1e6, 1e6), is(1e12));
    }

    @Test public void area_valoresMixtos() {
        assertThat(Rectangulo.calcularArea(1000000, 0.5), is(500000.0));
    }

    @Test public void area_precision() {
        assertThat(Rectangulo.calcularArea(0.333, 3), closeTo(0.999, 0.001));
    }

    @Test public void area_dosNumerosMuyDiferentes() {
        assertThat(Rectangulo.calcularArea(1e6, 0.0001), closeTo(100.0, 0.01));
    }
}
