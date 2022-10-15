import { PartialType } from '@nestjs/mapped-types';
import { CreateCompileDto } from './create-compile.dto';

export class UpdateCompileDto extends PartialType(CreateCompileDto) {}
