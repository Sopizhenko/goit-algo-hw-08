import heapq

def min_cost_to_connect_cables(cables):
	# Перетворюємо список довжин кабелів у мін-купу
	heapq.heapify(cables)
	
	total_cost = 0

	# Поки в купі більше одного елемента
	while len(cables) > 1:
		# Виймаємо два найменші елементи
		first = heapq.heappop(cables)
		second = heapq.heappop(cables)
		
		# Вартість з'єднання двох кабелів
		cost = first + second
		
		# Додаємо вартість до загальних витрат
		total_cost += cost
		
		# Додаємо новий кабель назад у купу
		heapq.heappush(cables, cost)
	
	return total_cost


if __name__ == "__main__":
	# Довжини кабелів
	cables = [5, 2, 3, 1, 4]
	result = min_cost_to_connect_cables(cables)
	print(f"Мінімальні витрати на об'єднання кабелів: {result}")