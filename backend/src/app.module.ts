import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { CompileModule } from './compile/compile.module';

@Module({
  imports: [CompileModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
