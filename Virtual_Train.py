class StationNode:
    def __init__(self, name):
        self.name, self.next, self.prev = name, None, None

class TrainRoute:
    def __init__(self, circular=False):
        self.head = self.tail = self.current = None
        self.circular = circular

    def add_station(self, name):
        new = StationNode(name)
        if not self.head:
            self.head = self.tail = self.current = new
            if self.circular:
                new.next = new.prev = new
        else:
            if self.circular:
                new.prev, new.next = self.tail, self.head
                self.tail.next, self.head.prev = new, new
            else:
                new.prev, self.tail.next = self.tail, new
            self.tail = new
        print(f"✅ Station added: {name}")

    def show_route(self, count=None):
        if not self.head:
            return print("🚫 No stations in the route.")
        names, cur = [self.head.name], self.head.next
        while cur and cur != self.head:
            names.append(cur.name)
            cur = cur.next
        if self.circular and count:
            names = (names * ((count // len(names)) + 1))[:count]
        print("➡ Route:", " -> ".join(names))

    def move(self, forward=True):
        if not self.current:
            return print("🚫 No stations.")
        self.current = (self.current.next if forward else self.current.prev) or (self.head if forward else self.tail)
        print(("⏩" if forward else "⏪"), "Train moved to:", self.current.name)

    def show_current(self):
        print(f"📍 Current Station: {self.current.name}" if self.current else "🚫 No current station.")


if __name__ == "__main__":
    print("===== 🚆 Doubly Linked Train Route =====")
    route = TrainRoute()
    for s in ["Station A", "Station B", "Station C", "Station D"]:
        route.add_station(s)

    route.show_route()
    route.show_current()
    route.move(); route.move(); route.move(forward=False)

    print("\n===== 🔄 Circular Metro Route =====")
    metro = TrainRoute(circular=True)
    for s in ["Metro X", "Metro Y", "Metro Z"]:
        metro.add_station(s)

    metro.show_route(count=6)
    metro.show_current()
    metro.move(); metro.move(); metro.move(); metro.move(forward=False)
