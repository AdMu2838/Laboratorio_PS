package ps.lab;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class IdentificadorNumeros {
    public static Map<String, List<Integer>> identificarParesImpares(List<Integer> numeros) {
        return numeros.stream().collect(Collectors.groupingBy(n -> n % 2 == 0 ? "Par" : "Impar"));
    }
}