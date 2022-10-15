import {
  Controller,
  Get,
  Post,
  Body,
  Patch,
  Param,
  Delete,
} from '@nestjs/common';
import { CompileService } from './compile.service';
import { CreateCompileDto } from './dto/create-compile.dto';

@Controller('compile')
export class CompileController {
  constructor(private readonly compileService: CompileService) {}

  @Post()
  create(@Body() createCompileDto: CreateCompileDto) {
    return this.compileService.create(createCompileDto);
  }
}
