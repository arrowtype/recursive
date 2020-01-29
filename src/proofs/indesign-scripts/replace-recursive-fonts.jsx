// Replace fonts in current INDD doc according to a set list
// Each line in theFontReplacements: 'Existing Font', 'Existing Style', 'New Font', 'New Style',
// Styles are optional - leave blank ('') if unwanted

// Sadly, does not work to replace variable font instances :(

var mydoc = app.activeDocument;


var theFontReplacements = [
  'Recursive b027st','Sans Linear Black','Recursive Sans Casual','Regular',
//   'Recursive Sans Casual','SemiBold','Recursive Sans Casual','Light',
//   'Recursive Mono Linear','SemiBold','Recursive Sans Casual','Regular',
  
];

for (i = 0; i < (theFontReplacements.length/4); i++) {

  app.findTextPreferences = NothingEnum.nothing;
  app.changeTextPreferences = NothingEnum.nothing;
  app.findTextPreferences.appliedFont = theFontReplacements[i*4];
  if (theFontReplacements[(i*4)+1] != ''){
    app.findTextPreferences.fontStyle = theFontReplacements[(i*4)+1];
  };
  app.changeTextPreferences.appliedFont  = theFontReplacements[(i*4)+2];
  if (theFontReplacements[(i*4)+3] != ''){
    app.changeTextPreferences.fontStyle  = theFontReplacements[(i*4)+3];
  };
  mydoc.changeText();

};
