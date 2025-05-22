package ps.lab;

import org.junit.Test;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.*;
import java.util.*;

public class IdentificadorNumerosTest {

    // Casos normales
    @Test public void paresImpares_mix() {
        List<Integer> entrada = Arrays.asList(1, 2, 3, 4);
        Map<String, List<Integer>> resultado = IdentificadorNumeros.identificarParesImpares(entrada);
        assertThat(resultado.get("Par"), containsInAnyOrder(2, 4));
        assertThat(resultado.get("Impar"), containsInAnyOrder(1, 3));
    }

    @Test public void todosPares() {
        List<Integer> entrada = Arrays.asList(2, 4, 6);
        Map<String, List<Integer>> resultado = IdentificadorNumeros.identificarParesImpares(entrada);
        assertThat(resultado.get("Par"), containsInAnyOrder(2, 4, 6));
        assertThat(resultado.containsKey("Impar"), is(false));
    }

    @Test public void todosImpares() {
        List<Integer> entrada = Arrays.asList(1, 3, 5);
        Map<String, List<Integer>> resultado = IdentificadorNumeros.identificarParesImpares(entrada);
        assertThat(resultado.get("Impar"), containsInAnyOrder(1, 3, 5));
        assertThat(resultado.containsKey("Par"), is(false));
    }

    @Test public void listaVacia() {
        Map<String, List<Integer>> resultado = IdentificadorNumeros.identificarParesImpares(Collections.emptyList());
        assertThat(resultado.isEmpty(), is(true));
    }

    // Casos con negativos
    @Test public void numerosNegativos() {
        List<Integer> entrada = Arrays.asList(-2, -3, -4);
        Map<String, List<Integer>> resultado = IdentificadorNumeros.identificarParesImpares(entrada);
        assertThat(resultado.get("Par"), containsInAnyOrder(-2, -4));
        assertThat(resultado.get("Impar"), containsInAnyOrder(-3));
    }

    // Casos mixtos
    @Test public void cerosYNegativos() {
        List<Integer> entrada = Arrays.asList(0, -1, -2);
        Map<String, List<Integer>> resultado = IdentificadorNumeros.identificarParesImpares(entrada);
        assertThat(resultado.get("Par"), containsInAnyOrder(0, -2));
        assertThat(resultado.get("Impar"), containsInAnyOrder(-1));
    }

    @Test public void ceros() {
        List<Integer> entrada = Arrays.asList(0, 0, 0);
        Map<String, List<Integer>> resultado = IdentificadorNumeros.identificarParesImpares(entrada);
        assertThat(resultado.get("Par"), contains(0, 0, 0));
    }

    // Casos con números repetidos
    @Test public void duplicados() {
        List<Integer> entrada = Arrays.asList(2, 2, 3, 3);
        Map<String, List<Integer>> resultado = IdentificadorNumeros.identificarParesImpares(entrada);
        assertThat(resultado.get("Par"), contains(2, 2));
        assertThat(resultado.get("Impar"), contains(3, 3));
    }

    // Casos extremos
    @Test public void extremosInt() {
        List<Integer> entrada = Arrays.asList(Integer.MAX_VALUE, Integer.MIN_VALUE);
        Map<String, List<Integer>> resultado = IdentificadorNumeros.identificarParesImpares(entrada);
        assertThat(resultado.get("Par"), contains(Integer.MIN_VALUE));
        assertThat(resultado.get("Impar"), contains(Integer.MAX_VALUE));
    }

    @Test public void listaUnElementoPar() {
        Map<String, List<Integer>> resultado = IdentificadorNumeros.identificarParesImpares(List.of(4));
        assertThat(resultado.get("Par"), contains(4));
    }

    @Test public void listaUnElementoImpar() {
        Map<String, List<Integer>> resultado = IdentificadorNumeros.identificarParesImpares(List.of(5));
        assertThat(resultado.get("Impar"), contains(5));
    }

    // Casos múltiples con diferentes longitudes
    @Test public void listaCon100Numeros() {
        List<Integer> entrada = new ArrayList<>();
        for (int i = 1; i <= 100; i++) entrada.add(i);
        Map<String, List<Integer>> resultado = IdentificadorNumeros.identificarParesImpares(entrada);
        assertThat(resultado.get("Par").size(), is(50));
        assertThat(resultado.get("Impar").size(), is(50));
    }

    @Test public void listaConUnSoloNumeroNegativo() {
        Map<String, List<Integer>> resultado = IdentificadorNumeros.identificarParesImpares(List.of(-1));
        assertThat(resultado.get("Impar"), contains(-1));
    }

    @Test public void listaConUnSoloNumeroCero() {
        Map<String, List<Integer>> resultado = IdentificadorNumeros.identificarParesImpares(List.of(0));
        assertThat(resultado.get("Par"), contains(0));
    }

    @Test public void listaSoloNegativos() {
        List<Integer> entrada = Arrays.asList(-1, -2, -3, -4);
        Map<String, List<Integer>> resultado = IdentificadorNumeros.identificarParesImpares(entrada);
        assertThat(resultado.get("Par"), contains(-2, -4));
        assertThat(resultado.get("Impar"), contains(-1, -3));
    }
}
