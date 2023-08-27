class ElectricSocket:
    def supply_electricity(self, voltage):
        print(f"Electric socket connected: {voltage}")


class USPlugAdapter:
    def supply_electricity(self, socket, voltage):
        print("Connect US plug using adapter")
        socket.supply_electricity(voltage)


europe_socket = ElectricSocket()
us_socket_adapter = USPlugAdapter()
us_socket_adapter.supply_electricity(europe_socket, 10)
