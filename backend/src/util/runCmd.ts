import { exec, spawn } from 'child_process';

export const runPython = async (filePath: string): Promise<string> => {
  return new Promise<string>((resolve, reject) => {
    const childProcess = spawn('python3', [filePath]);

    childProcess.stdout.on('data', (data) => {
      resolve(data.toString());

      childProcess.kill();
    });

    childProcess.stderr.on('data', (data) => {
      reject(data.toString());
      childProcess.kill();
    });
  });
};

export const runCpp = async (filePath: string): Promise<string> => {
  return new Promise<string>((resolve, reject) => {
    // const childProcess = spawn('g++', [filePath]);

    exec(`g++ ${filePath}`, (error, stdout, stderr) => {
      if (error) {
        console.error(`Error: ${error.message}`);
        reject(error.message);
        return;
      }
      if (stderr) {
        console.error(`STDERR: ${error.message}`);
        reject(error.message);
        return;
      }
      const runner = spawn(`${filePath}`);

      // inputs if any
      // TODO: Handle input from user

      runner.stdout.on('data', (data) => {
        resolve(data.toString());
      });

      runner.stderr.on('data', (data) => {
        reject(data.toString());
      });
      runner.stderr.on('error', (data) => {
        reject(data.toString());
      });
    });
  });
};

export const runJs = async (filePath: string): Promise<string> => {
  return new Promise<string>((resolve, reject) => {
    const runner = spawn('node', [filePath]);

    runner.stdout.on('data', (data) => {
      console.log(data);

      resolve(data.toString());
    });
    runner.stderr.on('data', (data) => {
      reject(data.toString());
    });
    runner.stderr.on('error', (data) => {
      reject(data.toString());
    });
  });
};

export const runTs = async (filePath: string): Promise<string> => {
  return new Promise<string>((resolve, reject) => {
    const runner = spawn(`ts-node ${filePath}`);

    runner.stdout.on('data', (data) => {
      resolve(data.toString());
    });
    runner.stderr.on('data', (data) => {
      reject(data.toString());
    });
    runner.stderr.on('error', (data) => {
      reject(data.toString());
    });
  });
};
