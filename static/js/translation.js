// Масив перекладів для трьох мов
var arrLang = {
  'en': {
    'about': 'About Us',
    'goods': 'Goods',
    'benefits': 'Benefits',
    'contact': 'Contact US',
    'home': 'Home',
    'all_employees': 'All employees',
    'all_words': 'All words',
    'all_categories': 'All categories',
    'search_words': 'Search words...'
  },
  'uk': {
    'about': 'Про нас',
    'goods': 'Товари',
    'benefits': 'Переваги',
    'contact': 'Контакти',
    'home': 'Головна',
    'all_employees': 'Всі співробітники',
    'all_words': 'Всі слова',
    'all_categories': 'Всі категорії',
    'search_words': 'Пошук слів...'
  },
  'pl': {
    'about': 'O nas',
    'goods': 'Produkty',
    'benefits': 'Korzyści',
    'contact': 'Kontakt',
    'home': 'Strona główna',
    'all_employees': 'Wszyscy pracownicy',
    'all_words': 'Wszystkie słowa',
    'all_categories': 'Wszystkie kategorie',
    'search_words': 'Szukaj słów...'
  }
};

// Функція для перекладу тексту
function translateText(lang) {
  $('.lang').each(function(index, item) {
    var key = $(this).attr('key');
    if (arrLang[lang] && arrLang[lang][key]) {
      $(this).text(arrLang[lang][key]);
    }
  });
  
  // Зберігаємо вибрану мову в localStorage
  localStorage.setItem('selectedLanguage', lang);
}

// Функція для встановлення мови при завантаженні сторінки
function setLanguageOnLoad() {
  var savedLang = localStorage.getItem('selectedLanguage');
  if (savedLang && arrLang[savedLang]) {
    translateText(savedLang);
  }
}

// Обробник кліків на кнопки перекладу
$(document).ready(function() {
  $('.translate').click(function() {
    var lang = $(this).attr('id');
    translateText(lang);
  });
  
  // Встановлюємо мову при завантаженні сторінки
  setLanguageOnLoad();
}); 