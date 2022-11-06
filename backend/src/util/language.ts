const extensionList = {
  'python': 'py',
  'c': 'c',
  'cpp': 'cpp',
  'c#': 'cs',
  'java': 'java',
  'javascript': 'js',
  'typescript': 'ts',
  'ruby': 'rb',
};
export const getExtension = (language: string): string => {
  return extensionList[language];
};
