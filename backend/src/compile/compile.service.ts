import { HttpException, Injectable } from '@nestjs/common';
import { CreateCompileDto } from './dto/create-compile.dto';
import { promises } from 'fs';
import { getExtension } from 'src/util/language';
import { spawn } from 'child_process';

@Injectable()
export class CompileService {
  public async create(createCompileDto: CreateCompileDto) {
    const { language, code } = createCompileDto;

    const fileName = `${language}-${Date.now()}.${getExtension(language)}`;
    const filePath = `${process.cwd()}/codes/${fileName}`;

    try {
      await promises.writeFile(filePath, code);

      const result = await this.compile(filePath);

      return {
        fileName,
        result,
      };
    } catch (err) {
      console.log(err);
      throw new HttpException(err, 500);
    }
  }
  public async compile(filePath: string) {
    console.log('Inside compile');

    try {
      const result = await this.runCommand(`${filePath}`);
      return result;
    } catch (err) {
      throw new HttpException('Compilation error' + err, 500);
    }
  }

  public async runCommand(filePath: string) {
    console.log(filePath);

    return new Promise((resolve, reject) => {
      const child = spawn('python3', [filePath]);
      child.stdout.on('data', (data) => {
        resolve(data.toString());
      });
      child.stderr.on('data', (data) => {
        reject(data.toString());
      });
    });
  }
}
