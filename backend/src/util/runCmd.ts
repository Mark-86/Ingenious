import { exec, spawn } from 'child_process';
import { promises } from 'fs';

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

    childProcess.on('exit', async () => {
      try {
        await promises.rm(filePath);
      } catch (err) {
        console.error(err);
      }
    });
  });
};

export const runCpp = async (filePath: string): Promise<string> => {
  return new Promise<string>((resolve, reject) => {
    let execPath = filePath.split('.')[0];

    exec(`g++ ${filePath} -o ${execPath}`, (error, stdout, stderr) => {
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
      const runner = spawn(`${execPath}`, []);

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

      runner.on('exit', async () => {
        await promises.rm(execPath);
        await promises.rm(filePath);
      });
    });
  });
};

export const runJs = async (filePath: string): Promise<string> => {
  let result = '';
  return new Promise<string>((resolve, reject) => {
    const runner = spawn('node', [filePath]);

    runner.stdout.on('data', (data) => {
      result += data.toString();
    });
    runner.stderr.on('data', (data) => {
      reject(data.toString());
    });
    runner.stderr.on('error', (data) => {
      reject(data.toString());
    });
    runner.on('exit', async () => {
      resolve(result);

      await promises.rm(filePath);
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
