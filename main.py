from typing import List, Tuple, Dict
import json


def calculate_panels(panel_width: int, panel_height: int, 
                    roof_width: int, roof_height: int) -> int:
    
    maximo_paneles = 0

    for ancho_p, alto_p in [(panel_width, panel_height), (panel_height, panel_width)]:
        print(ancho_p,alto_p)
        max_filas = roof_height // alto_p
        print(max_filas)

        for filas in range(max_filas + 1):
            
            altura_usada = filas * alto_p
            
            paneles_normales = filas * (roof_width // ancho_p)

            altura_restante = roof_height - altura_usada

            paneles_rotados = (altura_restante // ancho_p) * (roof_width // alto_p)

            total_paneles = paneles_normales + paneles_rotados
            maximo_paneles = max(maximo_paneles, total_paneles)

    return maximo_paneles

def run_tests() -> None:
    with open('test_cases.json', 'r') as f:
        data = json.load(f)
        test_cases: List[Dict[str, int]] = [
            {
                "panel_w": test["panelW"],
                "panel_h": test["panelH"],
                "roof_w": test["roofW"],
                "roof_h": test["roofH"],
                "expected": test["expected"]
            }
            for test in data["testCases"]
        ]
    
    print("Corriendo tests:")
    print("-------------------")
    
    for i, test in enumerate(test_cases, 1):
        result = calculate_panels(
            test["panel_w"], test["panel_h"], 
            test["roof_w"], test["roof_h"]
        )
        passed = result == test["expected"]
        
        print(f"Test {i}:")
        print(f"  Panels: {test['panel_w']}x{test['panel_h']}, "
              f"Roof: {test['roof_w']}x{test['roof_h']}")
        print(f"  Expected: {test['expected']}, Got: {result}")
        print(f"  Status: {'✅ PASSED' if passed else '❌ FAILED'}\n")


def main() -> None:
    print("🐕 Wuuf wuuf wuuf 🐕")
    print("================================\n")
    
    run_tests()


if __name__ == "__main__":
    main()
