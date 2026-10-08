LIMITES_DEMO_HORAS = {
	"tren de aterrizaje": 10000,
	"tren": 10000,
	"motor": 4000,
	"turbina": 3500,
	"compresor": 2500,
	"álabe": 2500,
	"alabe": 2500,
	"hélice": 3000,
	"helice": 3000,
	"apu": 3000,
	"freno": 1200,
	"neumático": 500,
	"neumatico": 500,
	"llanta": 500,
	"bomba": 2500,
	"generador": 3000,
	"filtro": 500
}
LIMITE_GENERAL_HORAS = 1000



def leer_numero(mensaje):
	while True:
		try:
			valor = float(input(mensaje))
			if valor < 0:
				print("El valor no puede ser negativo.")
			else:
				return valor
		except ValueError:
			print("Ingresa un número válido.")


def obtener_limite_horas(nombre_componente):
	nombre = nombre_componente.strip().lower()
	for palabra_clave in LIMITES_DEMO_HORAS:
		if palabra_clave in nombre:
			return LIMITES_DEMO_HORAS[palabra_clave]
	return LIMITE_GENERAL_HORAS


def buscar_aeronave(aeronaves, matricula):
	for aeronave in aeronaves:
		if aeronave["matricula"] == matricula:
			return aeronave
	return None


def registrar_aeronave(aeronaves):
	matricula = input("Matrícula: ").strip().upper()
	if buscar_aeronave(aeronaves, matricula) is not None:
		print("Ya existe una aeronave con esa matrícula.")
		return

	modelo = input("Modelo: ").strip()
	horas_vuelo = leer_numero("Horas de vuelo acumuladas: ")
	aeronave = {
		"matricula": matricula,
		"modelo": modelo,
		"horas_vuelo": horas_vuelo,
		"componentes": []
	}
	aeronaves.append(aeronave)
	print("Aeronave registrada.")


def registrar_componentes(aeronaves):
	matricula = input("Matrícula de la aeronave: ").strip().upper()
	aeronave = buscar_aeronave(aeronaves, matricula)
	if aeronave is None:
		print("No se encontró esa aeronave.")
		return

	while True:
		nombre = input("Nombre del componente: ").strip()
		limite_horas = obtener_limite_horas(nombre)
		print("Límite de ejemplo asignado: " + str(limite_horas) + " horas.")
		horas_uso = leer_numero("Horas de uso actuales: ")

		if horas_uso > limite_horas:
			print("MANTENIMIENTO NECESARIO: el componente superó su límite de horas.")
			while True:
				realizar_mantenimiento = input(
					"¿Deseas registrar el mantenimiento ahora? (s/n): "
				).strip().lower()
				if realizar_mantenimiento == "s":
					horas_uso = 0
					print("Mantenimiento registrado. Las horas de uso se reiniciaron a 0.")
					break
				if realizar_mantenimiento == "n":
					print("Mantenimiento pendiente; el componente continúa vencido.")
					break
				print("Responde s o n.")
		else:
			print("El componente no ha superado su límite de horas.")

		componente = {
			"nombre": nombre,
			"horas_uso": horas_uso,
			"limite_horas": limite_horas
		}
		aeronave["componentes"].append(componente)

		continuar = input("¿Registrar otro componente? (s/n): ").strip().lower()
		if continuar != "s":
			break


def ver_aeronaves_registradas(aeronaves):
	print("\n--- Aeronaves registradas ---")
	if not aeronaves:
		print("No hay aeronaves registradas.")
		return

	for aeronave in aeronaves:
		print(
			"Matrícula: "
			+ aeronave["matricula"]
			+ ", modelo: "
			+ aeronave["modelo"]
			+ ", horas de vuelo: "
			+ str(aeronave["horas_vuelo"])
		)


def ver_componentes_registrados(aeronaves):
	print("\n--- Componentes registrados ---")
	hay_componentes = False

	for aeronave in aeronaves:
		for componente in aeronave["componentes"]:
			print(
				"Aeronave "
				+ aeronave["matricula"]
				+ " ("
				+ aeronave["modelo"]
				+ "), componente: "
				+ componente["nombre"]
				+ ", horas de uso: "
				+ str(componente["horas_uso"])
				+ ", límite: "
				+ str(componente["limite_horas"])
				+ "."
			)
			hay_componentes = True

	if not hay_componentes:
		print("No hay componentes registrados.")


def consultar_mantenimiento(aeronaves):
	hay_componentes_vencidos = False
	print("\n--- Reporte de mantenimiento ---")

	for aeronave in aeronaves:
		for componente in aeronave["componentes"]:
			if componente["horas_uso"] > componente["limite_horas"]:
				print(
					"Mantenimiento inmediato: aeronave "
					+ aeronave["matricula"]
					+ " ("
					+ aeronave["modelo"]
					+ "), componente "
					+ componente["nombre"]
					+ ". Horas de uso: "
					+ str(componente["horas_uso"])
					+ ", límite: "
					+ str(componente["limite_horas"])
					+ "."
				)
				hay_componentes_vencidos = True

	if not hay_componentes_vencidos:
		print("No hay componentes que hayan superado su límite de horas.")


def main():
	aeronaves = []
	while True:
		print("\n=== Gestión de mantenimiento aeronáutico ===")
		print("1. Registrar aeronave")
		print("2. Registrar componentes")
		print("3. Consultar mantenimiento")
		print("4. Ver aeronaves registradas")
		print("5. Ver componentes registrados")
		print("6. Salir")
		opcion = input("Selecciona una opción: ").strip()

		if opcion == "1":
			registrar_aeronave(aeronaves)
		elif opcion == "2":
			registrar_componentes(aeronaves)
		elif opcion == "3":
			consultar_mantenimiento(aeronaves)
		elif opcion == "4":
			ver_aeronaves_registradas(aeronaves)
		elif opcion == "5":
			ver_componentes_registrados(aeronaves)
		elif opcion == "6":
			print("Programa finalizado.")
			break
		else:
			print("Opción no válida. Intenta de nuevo.")


main()
