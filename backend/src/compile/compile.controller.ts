import {
  Controller,
  Get,
  Post,
  Body,
  Patch,
  Param,
  Delete,
  HttpException,
} from '@nestjs/common';
import { CompileService } from './compile.service';
import { CreateCompileDto } from './dto/create-compile.dto';

@Controller('compile')
export class CompileController {
  constructor(private readonly compileService: CompileService) {}

  @Post()
  async create(@Body() createCompileDto: CreateCompileDto) {
    try {
      const output = await this.compileService.create(createCompileDto);
      return output;
    } catch (err) {
      throw new HttpException('Something went wrong', 500);
    }
  }
}
