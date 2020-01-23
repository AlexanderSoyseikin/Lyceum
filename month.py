def month_name(n, lang):
    en = ["january", "february",
          "march", "april",
          "may", "june", "july",
          "august", "september",
          "october", "november",
          "december"]
    ru = ["январь", "февраль",
          "март", "апрель",
          "май", "июнь",
          "июль", "август",
          "сентябрь", "октябрь",
          "ноябрь", "декабрь"]
    return locals()[lang][n - 1]
