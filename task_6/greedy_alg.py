def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )

    selected_items = []
    remaining_budget = budget

    for item, details in sorted_items:
        if details["cost"] <= remaining_budget:
            selected_items.append(item)
            remaining_budget -= details["cost"]

    return selected_items
