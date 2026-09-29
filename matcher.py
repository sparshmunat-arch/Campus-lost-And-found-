def calculate_similarity(lost_item, found_item):
    score = 0

    lost_name = lost_item[1].lower()
    found_name = found_item[1].lower()

    lost_description = lost_item[2].lower()
    found_description = found_item[2].lower()

    lost_location = lost_item[3].lower()
    found_location = found_item[3].lower()

    # Item name comparison
    if lost_name == found_name:
        score += 40
    elif lost_name in found_name or found_name in lost_name:
        score += 25

    # Description comparison
    lost_words = set(lost_description.split())
    found_words = set(found_description.split())

    common_words = lost_words.intersection(found_words)

    if len(common_words) >= 3:
        score += 30
    elif len(common_words) >= 1:
        score += 15

    # Location comparison
    if lost_location == found_location:
        score += 30
    elif lost_location in found_location or found_location in lost_location:
        score += 15

    return score