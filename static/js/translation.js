// Translation array for three languages
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
    'about': 'About Us',
    'goods': 'Goods',
    'benefits': 'Benefits',
    'contact': 'Contact',
    'home': 'Home',
    'all_employees': 'All employees',
    'all_words': 'All words',
    'all_categories': 'All categories',
    'search_words': 'Search words...'
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

// Function to translate text
function translateText(lang) {
  $('.lang').each(function(index, item) {
    var key = $(this).attr('key');
    if (arrLang[lang] && arrLang[lang][key]) {
      $(this).text(arrLang[lang][key]);
    }
  });
  
  // Save selected language in localStorage
  localStorage.setItem('selectedLanguage', lang);
}

// Function to set language on page load
function setLanguageOnLoad() {
  var savedLang = localStorage.getItem('selectedLanguage');
  if (savedLang && arrLang[savedLang]) {
    translateText(savedLang);
  }
}

// Click handler for translation buttons
$(document).ready(function() {
  $('.translate').click(function() {
    var lang = $(this).attr('id');
    translateText(lang);
  });
  
  // Set language on page load
  setLanguageOnLoad();
}); 