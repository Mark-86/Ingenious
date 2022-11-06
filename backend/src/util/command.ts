// TODO: Put the commands to run programs according to programming language specified

import { runCpp, runJs, runPython, runTs } from './runCmd';

const commands = {
  'python': runPython,
  'cpp': runCpp,
  'javascript': runJs,
  'typescript': runTs,
};

export const runCommand = async (language: string, filePath: string) => {
  return await commands[language](filePath);
};
