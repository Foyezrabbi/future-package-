class Math:
    @staticmethod
    def a_plus_b_whole_square(a, b):
        return (f"""
(a + b)² = a² + 2ab + b²")
         = ({a ** 2})² + {2 * a * b} + ({b ** 2})²
         = {a ** 2} + {2 * a * b} + {b ** 2}
         = {(a ** 2) + (2 * a * b) + (b ** 2)}
""")

    @staticmethod
    def a_minus_b_whole_square( a, b):
        return(f"""
(a + b)² = a² + 2ab + b²")
         = ({a ** 2})² - {2 * a * b} + ({b ** 2})²
         = {a ** 2} - {2 * a * b} + {b ** 2}
         = {(a ** 2) - (2 * a * b) + (b ** 2)}
""")


math = Math()
print(math.a_plus_b_whole_square(1, 2))
print(math.a_minus_b_whole_square(1, 2))
