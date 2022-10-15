import { Module } from '@nestjs/common';
import { CompileService } from './compile.service';
import { CompileController } from './compile.controller';

@Module({
  controllers: [CompileController],
  providers: [CompileService]
})
export class CompileModule {}
