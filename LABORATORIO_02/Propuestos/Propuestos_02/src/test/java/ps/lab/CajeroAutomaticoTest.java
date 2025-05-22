package ps.lab;

import org.junit.Before;
import org.junit.Test;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.*;

public class CajeroAutomaticoTest {

    private CajeroAutomatico cajero;

    @Before
    public void setUp() {
        cajero = new CajeroAutomatico(1000.0); // Saldo inicial
    }

    @Test
    public void testConsultarSaldoInicial() {
        assertThat(cajero.consultarSaldo(), is(1000.0));
    }

    @Test
    public void testDepositoValido() {
        cajero.depositar(200);
        assertThat(cajero.consultarSaldo(), is(1200.0));
    }

    @Test
    public void testRetiroValido() {
        cajero.retirar(300);
        assertThat(cajero.consultarSaldo(), is(700.0));
    }

    @Test(expected = IllegalArgumentException.class)
    public void testDepositoCero() {
        cajero.depositar(0);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testRetiroCero() {
        cajero.retirar(0);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testDepositoNegativo() {
        cajero.depositar(-50);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testRetiroNegativo() {
        cajero.retirar(-100);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testRetiroMayorQueSaldo() {
        cajero.retirar(1500);
    }

    @Test
    public void testRetiroExacto() {
        cajero.retirar(1000);
        assertThat(cajero.consultarSaldo(), is(0.0));
    }

    @Test
    public void testDepositoDecimal() {
        cajero.depositar(123.45);
        assertThat(cajero.consultarSaldo(), is(closeTo(1123.45, 0.001)));
    }

    @Test
    public void testRetiroDecimal() {
        cajero.retirar(87.25);
        assertThat(cajero.consultarSaldo(), is(closeTo(912.75, 0.001)));
    }

    @Test
    public void testMultiplesOperaciones() {
        cajero.depositar(100);
        cajero.retirar(50);
        cajero.depositar(200);
        cajero.retirar(100);
        assertThat(cajero.consultarSaldo(), is(1150.0));
    }

    @Test
    public void testSaldoSinOperaciones() {
        assertThat(cajero.consultarSaldo(), is(1000.0));
    }

    @Test
    public void testDepositoGrande() {
        cajero.depositar(1_000_000);
        assertThat(cajero.consultarSaldo(), is(1_001_000.0));
    }

    @Test(expected = IllegalArgumentException.class)
    public void testCrearCajeroConSaldoNegativo() {
        new CajeroAutomatico(-100);
    }

    @Test
    public void testDepositoMuyPequeño() {
        cajero.depositar(0.01);
        assertThat(cajero.consultarSaldo(), is(closeTo(1000.01, 0.001)));
    }
}
