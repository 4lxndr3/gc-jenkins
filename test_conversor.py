import conversor

def test_fahrenheit_para_celsius():
    # Testa se 32°F se converte corretamente para 0°C
    assert conversor.fahrenheit_para_celsius(32) == 0

def test_celsius_para_fahrenheit():
    # Testa se 100°C se converte corretamente para 212°F
    assert conversor.celsius_para_fahrenheit(100) == 212